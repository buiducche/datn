import { Controller, Get, Param, Post, Query, Render, Res, Body } from '@nestjs/common';
import { Response } from 'express';
import * as path from 'path';
import { ApiOkResponse, ApiTags } from '@nestjs/swagger';

@ApiTags('Cycle')
@Controller('cycle')
export class CycleController {

  @Get()
  @Render('cycle')
  getTred() {
    return { message: 'Hello world!' };
  }

  @Post()
  @Render('cycle')
  async compareTred(@Body('courseID') courseID: string) {
    return { courseID };
  }

  @Get('download')
  downloadFile(@Res() res: Response): void {
    const filePath = path.join(__dirname,'..', 'public', 'logdata', 'find_cycle.log');
    res.setHeader('Content-disposition', 'attachment; filename=log.txt');
    res.setHeader('Content-type', 'text/plain');
    res.download(filePath, 'find_cycle.log', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
}