from itertools import combinations, product

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.utils.deltar import deltaR
from pdb import set_trace

import PhysicsTools.HeppyCore.framework.config as cfg

class TriggerInfo(object):
    def __init__(self, name, index, fired=True, prescale=1.):
        self.name = name
        self.index = index
        self.fired = fired
        self.prescale = prescale
        self.objects = []
        self.objIds = set()
        self.object_names = []

    def __str__(self):
        return 'TriggerInfo: name={name}, fired={fired}, n_objects={n_o}'.format(
            name=self.name, fired=self.fired, n_o=len(self.objects))

class TriggerAnalyzer(Analyzer):
    '''Access to trigger information, and trigger selection. The required
    trigger names need to be attached to the components.'''

    def declareHandles(self):
        super(TriggerAnalyzer, self).declareHandles()

        self.handles['triggerResultsHLT'  ] = AutoHandle(('TriggerResults', '', 'HLT'),'edm::TriggerResults')

        self.handles['triggerObjects_slim'] = AutoHandle('slimmedPatTrigger' , 'std::vector<pat::TriggerObjectStandAlone>')
        self.handles['triggerObjects_sel' ] = AutoHandle('selectedPatTrigger', 'std::vector<pat::TriggerObjectStandAlone>')
 
        self.handles['triggerPrescales'   ] =  AutoHandle('patTrigger', 'pat::PackedTriggerPrescales')
 
    def beginLoop(self, setup):
        super(TriggerAnalyzer,self).beginLoop(setup)

        self.triggerList = self.cfg_comp.triggers
        self.triggerObjects = []
        self.extraTriggerObjects = []
        if hasattr(self.cfg_comp, 'triggerobjects'):
            self.triggerObjects = self.cfg_comp.triggerobjects
        if hasattr(self.cfg_ana, 'extraTrig'):
            self.extraTrig = self.cfg_ana.extraTrig
        else:
            self.extraTrig = []
        if hasattr(self.cfg_ana, 'extraTrigObj'):
            self.extraTriggerObjects = self.cfg_ana.extraTrigObj

        self.vetoTriggerList = []

        if hasattr(self.cfg_comp, 'vetoTriggers'):
            self.vetoTriggerList = self.cfg_comp.vetoTriggers
            
        self.counters.addCounter('Trigger')
        self.counters.counter('Trigger').register('All events')
        self.counters.counter('Trigger').register('HLT')
                
        for trigger in set(['_'.join(trig.split('_')[:-1]) for trig in self.triggerList]):
            self.counters.counter('Trigger').register(trigger)
        for trigger in set(['_'.join(trig.split('_')[:-1]) for trig in self.triggerList]):
            self.counters.counter('Trigger').register(trigger + ' prescaled')
        for trigger in set(['_'.join(trig.split('_')[:-1]) for trig in self.vetoTriggerList]):
            self.counters.counter('Trigger').register('failed veto ' + trigger)

    def removeDuplicates(self, trigger_infos):
        # RIC: remove duplicated trigger objects 
        #      (is this something that may happen in first place?)
        for info in trigger_infos:
            objs = info.objects     
            for to1, to2 in combinations(info.objects, 2):
                to1Filter = set(sorted(list(to1.filterLabels())))
                to2Filter = set(sorted(list(to2.filterLabels())))
                if to1Filter != to2Filter:
                    continue
                dR = deltaR(to1.eta(), to1.phi(), to2.eta(), to2.phi())
                if dR<0.01 and to2 in objs:
                    objs.remove(to2)
            info.objects = objs

    def process(self, event):
        self.readCollections(event.input)
        
        event.run = event.input.eventAuxiliary().id().run()
        event.lumi = event.input.eventAuxiliary().id().luminosityBlock()
        event.eventId = event.input.eventAuxiliary().id().event()

        triggerBits = self.handles['triggerResultsHLT'].product()
        names = event.input.object().triggerNames(triggerBits)
        
        event.triggerResults = triggerBits

        preScales = self.handles['triggerPrescales'].product()

        self.counters.counter('Trigger').inc('All events')

        trigger_passed = False

        if not self.triggerList:
            return True

        trigger_infos = []
        triggers_fired = []
        
        for trigger_name in self.triggerList + self.extraTrig:
            trigger_name_no_version = '_'.join(trigger_name.split('_')[:-1])
            index = names.triggerIndex(trigger_name)
            if index == len(triggerBits):
                continue
            prescale = preScales.getPrescaleForIndex(index)
            fired = triggerBits.accept(index)

            trigger_infos.append(TriggerInfo(trigger_name, index, fired, prescale))

            #print trigger_name, fired, prescale
            #if fired:
            #    import pdb ; pdb.set_trace()
            if fired and (prescale == 1 or self.cfg_ana.usePrescaled):
                if trigger_name in self.triggerList:
                    trigger_passed = True
                    self.counters.counter('Trigger').inc(trigger_name_no_version)            
                triggers_fired.append(trigger_name)
            elif fired:
                print 'WARNING: Trigger not passing because of prescale', trigger_name
                self.counters.counter('Trigger').inc(trigger_name_no_version + ' prescaled')

        # JAN: I don't understand why the following is needed - there is a 
        # unique loop above
        # self.removeDuplicates(trigger_infos)


        if self.cfg_ana.requireTrigger:
            if not trigger_passed:
                return False
                
        if self.cfg_ana.addTriggerObjects:
            try:
                triggerObjects = self.handles['triggerObjects_slim'].product()
            except:
                # print 'Cannot find the collection std::vector<pat::TriggerObjectStandAlone> labeled as "slimmedPatTrigger" ==> replacing with "selectedPatTrigger"...' 
                triggerObjects = self.handles['triggerObjects_sel' ].product()
                
            for to in triggerObjects:
                # unpack filter labels if needed (in 2017 it is)
                if getattr(self.cfg_ana, 'unpackLabels', False):
                    to.unpackFilterLabels(event.input.events.object(), triggerBits)
                to.unpackPathNames(names)
                for info in trigger_infos:
                    if to.hasPathName(info.name):
                        if to in info.objects:
                            continue
                        # print 'TO name', [n for n in to.filterLabels()], to.hasPathName(info.name, False)
                        if self.triggerObjects or self.extraTriggerObjects:
                            if not any(n in to.filterLabels() for n in self.triggerObjects + self.extraTriggerObjects):
                                continue
                            info.object_names.append([obj_n for obj_n in self.triggerObjects if obj_n in to.filterLabels()])
                        else:
                            info.object_names.append('')
                        info.objects.append(to)
                        info.objIds.add(abs(to.pdgId()))
                         
        event.trigger_infos = trigger_infos
        
        for itrig, iveto in product(event.trigger_infos, self.vetoTriggerList):
            if iveto == itrig.name and itrig.fired:
                trigger_name_no_version = '_'.join(itrig.name.split('_')[:-1])
                self.counters.counter('Trigger').inc('failed veto' + trigger_name_no_version)
                return False
        
        if self.cfg_ana.verbose:
            print 'run %d, lumi %d,event %d' %(event.run, event.lumi, event.eventId) , 'Triggers_fired: ', triggers_fired  
        if hasattr(self.cfg_ana, 'saveFlag'):
            if self.cfg_ana.saveFlag:
                setattr(event, 'tag', False)    
                setattr(event, 'probe', False)
                for trig in self.triggerList:
                    if trig in triggers_fired:
                        setattr(event, 'tag', True)    
                        break
                for trig in self.extraTrig:
                    if trig in triggers_fired:
                        setattr(event, 'probe', True)
                        break

        self.counters.counter('Trigger').inc('HLT')
        return True

    def __str__(self):
        tmp = super(TriggerAnalyzer,self).__str__()
        triglist = str(self.triggerList)
        return '\n'.join([tmp, triglist])

setattr(TriggerAnalyzer, 'defaultConfig', 
    cfg.Analyzer(
        class_object=TriggerAnalyzer,
        requireTrigger=True,
        usePrescaled=False,
        addTriggerObjects=True,
        # vetoTriggers=[],
    )
)
