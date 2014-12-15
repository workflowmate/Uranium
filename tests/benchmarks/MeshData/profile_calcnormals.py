from UM.Mesh.MeshData import MeshData

@profile
def calcNormals(mesh):
    mesh.calculateNormals()

mesh = MeshData()
mesh.reserveVertexCount(99999)
for i in range(33333):
    mesh.addVertex(0, 1, 0)
    mesh.addVertex(1, 1, 0)
    mesh.addVertex(1, 0, 0)

for i in range(100):
    calcNormals(mesh)
