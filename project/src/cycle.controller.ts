import { Controller, Get, Param, Post, Query, Render, Res, Body } from '@nestjs/common';
import { Response } from 'express';
import * as path from 'path';
import { ApiOkResponse, ApiTags } from '@nestjs/swagger';
import { SearchService } from './search/search.service';

@ApiTags('Cycle')
@Controller('cycle')
export class CycleController {
  constructor(
    private readonly searchService: SearchService,
  ) {}

  @Get()
  @Render('cycle')
  getTred() {
    return { message: 'Hello world!' };
  }

  @Post()
  @Render('cycle')
  async compareTred(@Body('courseID') courseID: string) {
    await this.searchService.createByCourseID(courseID,'cycle')
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