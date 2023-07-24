import { Controller, Get, Post, Put, Delete, Param, Body, Res, Render } from '@nestjs/common';
import { CourseService } from './course.service';
import { Course } from './course.entity';
import * as path from 'path';
import { Response } from 'express';
import { ApiTags } from '@nestjs/swagger';

@ApiTags('Course')
@Controller('course')
export class CourseController {
  constructor(private readonly coursesService: CourseService) {}

  @Get()
  async findAll(): Promise<Course[]> {
    return this.coursesService.findAll();
  }

  @Get(':courseID')
  @Render('course')
  async findOne(@Param('courseID') courseID: string): Promise<{course : Course}> {
    const coursedata = await this.coursesService.findBymaHocPhan(courseID)
    return { course : coursedata } ;
  }

  // @Post()
  // async create(@Body() course: Course): Promise<Course> {
  //   return this.coursesService.create(course);
  // }

  // @Put(':id')
  // async update(@Param('id') id: number, @Body() course: Course): Promise<void> {
  //   await this.coursesService.update(id, course);
  // }

  // @Delete(':id')
  // async delete(@Param('id') id: number): Promise<void> {
  //   await this.coursesService.delete(id);
  // }
}