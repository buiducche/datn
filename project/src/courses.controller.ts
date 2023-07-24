import { Controller, Get, Param, Render, Res } from '@nestjs/common';
import { Response } from 'express';
import * as path from 'path';
import { ApiOkResponse, ApiTags } from '@nestjs/swagger';

@ApiTags('Courses')
@Controller('courses')
export class CoursesController {
  private courses = [
    {
      id: 1,
      maHocPhan: 'Introduction to NestJS',
      tenHocPhan: 'Learn the basics of NestJS',
      thoiLuong: ['Controllers', 'Providers', 'Modules']
    },
    {
      id: 2,
      maHocPhan: 'Building a REST API with NestJS',
      tenHocPhan: 'Learn how to build a RESTful API with NestJS',
      thoiLuong: ['Controllers', 'Providers', 'Modules', 'Middleware']
    }
  ];

  @Get()
  getAllCourses() {
    return this.courses;
  }

  @Get(':id')
  @Render('course')
  getCourseById(@Param('id') id: string) {
    const course = this.courses.find(course => course.id === parseInt(id));
    return  course ;
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