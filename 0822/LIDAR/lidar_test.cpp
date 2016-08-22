/* 
Sample program for libMesaSR
Target Device: SwissRanger SR4500 Time-of-Flight camera

@author  Taiki Mashimo <mashimo.taiki@ac.jaxa.jp>
@date    2016-08-13

Compile:
    $ make
or
    $ g++ -o lidar_test lidar_test.cpp -lmesasr
Usage:
    $ ./lidar_test
*/

#include "stdio.h"
#include "stdlib.h"
#include <fstream>
#include "libMesaSR.h"

int main() {

  CMesaDevice* srCam=0;
  int res;

  //--------- Connect LIDAR ---------
  //ここにバージョン取得の関数を書く

  //--------- Connect LIDAR ---------
  SR_OpenETH(&srCam, "192.168.201.41");

  //--------- Set Acquire Mode ---------
  int mode = AM_COR_FIX_PTRN|AM_CONV_GRAY|AM_DENOISE_ANF; //recommended mode
  SR_SetMode(srCam, mode);
  printf("Acquire mode: %d \n", mode);

  //--------- Get Distance Data ---------
  ImgEntry* imgEntryArray;
  //ここに距離データ取得の関数を書く

  //--------- Get Rows & Cols ---------
  int rows, cols;
  rows=SR_GetRows(srCam);
  cols=SR_GetCols(srCam);
  printf("rows: %d cols: %d \n", rows, cols);

  //--------- Transform sphirical coodinate to xyz coordinate(Do not edit)---------
  int pitch = sizeof(short);
  short* X = (short*)(malloc(rows * cols * pitch));
  short* Y = (short*)(malloc(rows * cols * pitch));
  short* Z = (short*)(malloc(rows * cols * pitch));
  SR_CoordTrfUint16(srCam, X, Y, (unsigned short*)Z, pitch, pitch, pitch);

  //--------- Output only first 5 data(Do not edit) ---------
  printf("Distance data (x,y,z), with mm unit:\n");
  int j;
  for(j=0; j<5; j++) { 
  printf("%d %d %d\n", X[j], Y[j], Z[j]);
  }

  //--------- Output into PLY file(Do not edit) ---------
  std::ofstream ofs("lidar_data.ply");

  // write header
  ofs << "ply" << std::endl;
  ofs << "format ascii 1.0" << std::endl;
  ofs << "element vertex " <<  rows*cols-1 << std::endl;
  ofs << "property float x" << std::endl;
  ofs << "property float y" << std::endl;
  ofs << "property float z" << std::endl;
  ofs << "end_header"  << std::endl;

  // write contents
  int i;
  for(i=0; i<rows*cols-1; i++) {
    ofs << X[i] << " " << Y[i] << " " << Z[i] << std::endl;
  }

  ofs.close();

  //--------- Deconnect LIDAR(Do not edit) ---------
  SR_Close(srCam);

  return 0;

}
