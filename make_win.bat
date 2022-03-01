
mkdir build_win64 & pushd build_win64
cmake -G "Visual Studio 14 2015 Win64" ..
popd
cmake --build build_win64 --config Release 
pause
