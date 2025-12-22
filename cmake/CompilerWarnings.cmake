# from here:
#
# https://github.com/lefticus/cppbestpractices/blob/master/02-Use_the_Tools_Available.md
#
# modified version by Bastian Gonzalez Acevedo

function(set_target_warnings target_name)
	if(MSVC)
		target_compile_options(${target_name} PRIVATE
			/W4 /w14242 /w14254 /w14263 /w14265 /w14287 /we4289 
			/w14296 /w14311 /w14545 /w14546 /w14547 /w14549 /w14555 
			/w14619 /w14640 /w14826 /w14905 /w14906 /w14928 /permissive- /WX
		)
	elseif(CMAKE_CXX_COMPILER_ID MATCHES ".*Clang")
		target_compile_options(${target_name} PRIVATE 
			-Wall -Wextra -Wshadow -Wnon-virtual-dtor -Wold-style-cast 
			-Wcast-align -Wunused -Woverloaded-virtual -Wpedantic -Wconversion 
			-Wsign-conversion -Wnull-dereference -Wdouble-promotion -Wformat=2 
			-Wimplicit-fallthrough -Werror
		)
	elseif(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
		target_compile_options(${target_name} PRIVATE 
			-Wall -Wextra -Wshadow -Wnon-virtual-dtor -Wold-style-cast 
			-Wcast-align -Wunused -Woverloaded-virtual -Wpedantic -Wconversion 
			-Wsign-conversion -Wnull-dereference -Wdouble-promotion -Wformat=2 
			-Wimplicit-fallthrough -Werror -Wmisleading-indentation -Wduplicated-cond 
			-Wduplicated-branches -Wlogical-op -Wuseless-cast
		)
	else()
		message(AUTHOR_WARNING "No compiler warnings set for CXX compiler: '${CMAKE_CXX_COMPILER_ID}'")
		# TODO support Intel compiler
	endif()
endfunction()
