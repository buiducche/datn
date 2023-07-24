import { Controller, Get, Param, Post, Query, Render, Res, Body } from '@nestjs/common';
import { Response } from 'express';
import * as path from 'path';
import { ApiOkResponse, ApiTags } from '@nestjs/swagger';

@ApiTags('Tred')
@Controller('tred')
export class TredController {

  @Get()
  @Render('tred')
  getTred() {
    return { message: 'Hello world!' };
  }

  @Post()
  @Render('tred')
  async compareTred(@Body('courseID') courseID: string) {
    return { courseID };
  }

  @Get('download')
  downloadFile(@Res() res: Response): void {
    const filePath = path.join(__dirname,'..', 'public', 'logdata', 'transitive_reduction2023-07-01_20-13-53.log');
    res.setHeader('Content-disposition', 'attachment; filename=log.txt');
    res.setHeader('Content-type', 'text/plain');
    res.download(filePath, 'transitive_reduction2023-07-01_20-13-53.log', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }

  @Get(':id/image0tred')
  getCourseImageTred(@Param('id') id: string, @Res() res: Response) {
    // Logic to fetch the course image based on the ID
    // ...
    const imagePath = path.join(__dirname, '..', 'public', 'graph0tred', `${id}.svg`);
    return res.sendFile(imagePath);
  }

  @Get(':id/image0origin')
  getCourseImageOrigin(@Param('id') id: string, @Res() res: Response) {
    // Logic to fetch the course image based on the ID
    // ...
    const imagePath = path.join(__dirname, '..', 'public', 'graph0origin', `${id}.svg`);
    return res.sendFile(imagePath);
  }
}