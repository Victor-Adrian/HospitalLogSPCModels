import pm4py

#Logs and models for the compared subpopulations (created/filtered using ProM 6)
log_M16_under = "M16/MM16 Filtered for trace length (6-100) under 55 (0325 0325) no empty traces.xes"
log_M16_over = "M16/M16 Filtered for trace length (6-100) over 55 (0325 0325) no empty traces.xes"
model_M16_under = "M16/Petri - M16 Filtered for trace length (6-100) under 55 (0325 0325) no big skips.pnml"
model_M16_over = "M16/Petri - M16 Filtered for trace length (6-100) over 55 (0325 0325) no big skips.pnml"

log_M14_under = "M14/M14 Filtered for trace length (5-50) under 60 (080 050) no empty traces.xes"
log_M14_over = "M14/M14 Filtered for trace length (5-50) over 60 (060 030) no empty traces.xes"
model_M14_under = "M14/Petri - M14 Filtered for trace length (5-50) under 60 (080 050) no big skips.pnml"
model_M14_over = "M14/Petri - M14 Filtered for trace length (5-50) over 60 (060 030).pnml"

#Parameters for the enhanced version of token-based replay
opt_parameters = {
    'reach_mark_through_hidden': True,
    'stop_immediately_unfit': False,
    'walk_through_hidden_trans': True,
    'cleaning_token_flood': True
}

log = pm4py.read_xes(log_M14_under)
(model, im, fm) = pm4py.read_pnml(model_M14_over)

results = pm4py.fitness_token_based_replay(log, model, im, fm)
print(results)
