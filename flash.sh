dir=`pwd`
pushd ${OPENOCD_PATH}
./bin/openocd -f scripts/board/st_nucleo_f4.cfg -c "program $dir/BUILD/STM32_Button_Debounce.hex reset exit"
popd
