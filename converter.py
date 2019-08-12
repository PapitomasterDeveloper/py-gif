import imageio
import os

clip = os.path.abspath('hip-thrust.mp4')

def gifMaker(inputPath, targetFormat):

	outputPath = os.path.splitext(inputPath)[0] + targetFormat
	print('Converting ' + inputPath + ' to \n ' + outputPath)
	reader = imageio.get_reader(inputPath)
	# print(reader)
	fps = reader.get_meta_data()['fps']
	writer = imageio.get_writer(outputPath, fps=fps)

	for image in reader:
		writer.append_data(frames)
		print('Frame' + str(frames))
	print('Done!')
	writer.close()

gifMaker(clip,'.gif')
