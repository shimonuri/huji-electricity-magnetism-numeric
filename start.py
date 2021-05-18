import relaxation_model
rmax = 8
zmax = 14

model = relaxation_model.RelaxationModel(8, 14, 0.1, 0.1)
model.initDatabase()
matrix = model.space._convert_space_into_matrix()
model.space.create_map()
