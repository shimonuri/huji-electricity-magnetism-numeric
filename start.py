import relaxation_model

model = relaxation_model.RelaxationModel(8, 14, 0.05, 0.1)
model.initDatabase()
model.relax("result.pickle")
