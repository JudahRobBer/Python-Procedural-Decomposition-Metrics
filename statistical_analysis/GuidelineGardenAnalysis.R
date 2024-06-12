NotAI = subset(hw2_garden, id != "s2" )
NotAI = subset(NotAI, global_code_volume != 238)

Decent = subset(NotAI, Label > 2)

Good = subset(NotAI, Label > 3)

Great = subset(NotAI, Label > 4)

model = lm(Label ~ largest_information_function + global_code_volume + multiple_output_functions + reused_nodes,data = NotAI)
summary(model)

model = lm(Label ~ largest_information_function + global_code_volume + multiple_output_functions + reused_nodes, data = Decent)
model = lm(Label ~ largest_information_function + global_code_volume + multiple_output_functions + reused_nodes, data = Good)
model = lm(Label ~ largest_information_function + global_code_volume + multiple_output_functions + reused_nodes, data = Great)


hist(NotAI$largest_information_function)
hist(NotAI$multiple_output_functions)
hist(NotAI$global_code_volume)
hist(NotAI$reused_nodes)

NotAI$predicted = predict.lm(model,NotAI)
NotAI$predictdifference = NotAI$predicted - NotAI$Label

boxplot(largest_information_function ~ Label, data = NotAI)
boxplot(global_code_volume ~ Label, data = NotAI)

ai_ids = c("s2","s8","s31")
NotAI = subset(hw2_garden, !(id %in% ai_ids))
NotAI = subset(NotAI, global_code_volume != 238)

model = lm(score ~ largest_information_function + global_code_volume + multiple_output_functions + reused_nodes, data = NotAI)
summary(model)


notAI#predicted
