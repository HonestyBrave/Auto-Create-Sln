import os
import time
import subprocess

CMAKE_LIST_TXT = "CMakeLists.txt"
COMMON_DIRECTOR = "./"

def create_sln():
	time_str = str(int(time.time()))
	print("time_str: " + time_str)

	#create time director
	file_director = "../" + time_str
	os.mkdir(file_director)

	# create time.cpp and write common include files
	cpp_file = open(file_director + "/" + time_str +".cpp", "w+")
	with open(COMMON_DIRECTOR + "include_common.txt", "r") as common_file_to_read:
		for line in common_file_to_read.readlines():
			cpp_file.write(line)
	cpp_file.close()

	print("==== " + time_str + ".cpp create success!")

	# create common CMakeList.txt
	cmake_list = open(file_director + "/" + CMAKE_LIST_TXT, "w+")
	with open(COMMON_DIRECTOR + "CMakeLists_common.txt", "r") as common_file_to_read:
		for line in common_file_to_read.readlines():
			if "ADD_EXECUTABLE" in line:
				line = "ADD_EXECUTABLE(main %s.cpp)" %time_str
			cmake_list.write(line)
	cmake_list.close()

	print("==== CMakeLists.txt create success!")

	# create build director
	os.mkdir(file_director + "_build")

	# change director, then will generator in the file_director_build
	os.chdir(file_director + "_build")
	dest_path = os.getcwd() + "/../" + time_str
	cmd = ["cmake", "-A", "x64", dest_path]
	subprocess.call(cmd, shell = True)

if __name__ == "__main__":
	create_sln()



