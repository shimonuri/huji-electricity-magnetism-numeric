import relaxation_model

model = relaxation_model.RelaxationModel(8, 14, 0.1, 0.1)
model.initDatabase()
model.relax("result.pickle")
