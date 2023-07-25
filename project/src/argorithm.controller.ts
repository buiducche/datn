import { Controller, Get, Query, Body, Post, Res } from '@nestjs/common';
import { exec, spawn } from 'child_process';
import { ApiOkResponse, ApiTags } from '@nestjs/swagger';
import * as path from 'path';
import { Response } from 'express';


@ApiTags('Argorithm')
@Controller('argorithm')
export class ArgorithmController {
    @Get('add')
    async addNumbers(@Query('a') a: number, @Query('b') b: number): Promise<number> {
      const scriptPath = path.join(__dirname, '..', 'public', 'argorithm', 'test.py');
      const command = `python ${scriptPath} ${a} ${b}`;
  
      return new Promise<number>((resolve, reject) => {
        exec(command, (error, stdout, stderr) => {
          if (error) {
            reject(error);
          } else {
            const result = parseInt(stdout);
            resolve(result);
          }
        });
      });
    }

    @Get('ImportantSubject')
    async ImportantSubject(@Query('MSSV') MSSV: string): Promise<string> {
      const scriptPath = path.join(__dirname, '..', 'public', 'argorithm', 'ImportantSubject.py');
      const command = `python ${scriptPath} ${MSSV}`;
  
      return new Promise<string>((resolve, reject) => {
        exec(command, (error, stdout, stderr) => {
          if (error) {
            reject(error);
          } else {
            const result = stdout;
            resolve(result);
          }
        });
      });
    }

    @Get('gentree_personal')
    async GentreetSubject(@Query('MSSV') MSSV: string, @Res() res: Response){
      const scriptPath = path.join(__dirname, '..', 'public', 'argorithm', 'gentree_personal.py');
      const command = `python ${scriptPath} ${MSSV}`;
      await exec(`python ${scriptPath} ${MSSV}`);
      const imagePath = path.join(__dirname, '..', 'public', 'assets','graphP', `${MSSV}.png`);
      return res.sendFile(imagePath);
    }
}