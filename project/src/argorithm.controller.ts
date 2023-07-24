import { Controller, Get, Query, Body, Post } from '@nestjs/common';
import { exec, spawn } from 'child_process';
import { ApiOkResponse, ApiTags } from '@nestjs/swagger';
import * as path from 'path';

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
}