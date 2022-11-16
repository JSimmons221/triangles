import make_images as mi
import neural_network as nn
import shapes as shp

shp.make_data(5000, r'resources/triangles.csv')
print("made triangles")
mi.csv_to_images(r'resources/triangles.csv')
print("made images")
data, target = nn.load_my_fancy_dataset()
print("created dataset")
nn.train(data, target)
print("done")

