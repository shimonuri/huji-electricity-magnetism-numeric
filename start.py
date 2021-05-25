import relaxation_model

model = relaxation_model.RelaxationModel(8, 14, 0.1, 0.1)
model.initDatabase()
matrix = model.space._convert_space_into_matrix()
model.relax("result.pickle")
