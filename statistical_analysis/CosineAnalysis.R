CleanedCosine = subset(hw2_garden, Label != 0)
CleanedCosine = subset(CleanedCosine, global_code_volume != 238)

model = lm(Label ~ cos.similarity, data = CleanedCosine)
summary(model)
