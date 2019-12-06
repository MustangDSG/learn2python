import os
import struct

#const - взято из кода на си
maxSectors = 0xFF
bytesPerSector = 0x100
pixelsPerByte = 0x8

dataOffset = 0x0A
widthOffset = 0x12
heightOffset = 0x16

maxSizeSprite = maxSectors * bytesPerSector


print("All files and [sizes] in current directory, max size of sprite is " + str(maxSectors) + " TR-DOS sectors, " + str(bytesPerSector) + " bytes per sector or " + str(maxSizeSprite) + " bytes.\n")

def get_bmp_files():
	'''  Пробегаем по папкам и подпапкам в поисках файлов с расширением .bmp '''
	bmp_files = []
	for root, subfolders, files in os.walk(os.getcwd()):
		for file in files:
			if file.split(".")[-1] == "bmp":
				bmp_files.append(os.path.join(root, file))
	return bmp_files

def main():
	''' Основной код '''
	files = get_bmp_files()	
	for i in range(len(files)):
		file = open(files[i], "rb")
		data = file.read()
		fSize = os.path.getsize(files[i])
		
		width, height = struct.unpack("=ii", data[18:26])
		print(width, height)

		if fSize > maxSizeSprite:
			print("Warning, file size for " + str(file) + " is more than 255 sectors for TR-DOS.\n")

		else:
			if width % pixelsPerByte or height % pixelsPerByte:
				print("Warning, one or both sizes of pixel array aren't multiplying by 8 (pixels per byte).")
				print("File : " + str(file) + "\n")
			else:
				print("File " + str(file) + " dimensions are : " + str(width) + "x" + str(height) + "\n")


				pixelDataSize = struct.unpack("=i", data[34:38])
				headerSize = fSize - pixelDataSize[0]
				print(headerSize, pixelDataSize[0])

				with open("test", "wb") as f:	#имя выходного файла пока без переменной
					f.write(data[headerSize::])
				
		file.close()

if __name__ == '__main__':
	main()   #запускаем main при старте программы из консоли.