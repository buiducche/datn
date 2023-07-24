import { Get, Controller, Render, Post, Body } from '@nestjs/common';
import { CourseService } from './course/course.service';
import { Course } from './course/course.entity';

@Controller()
export class AppController {
  constructor(private readonly coursesService: CourseService) {}

  @Get()
  @Render('index')
  root() {
    return { message: 'Hello world!' };
  }

  @Post()
  @Render('index')
  async search(@Body('courseID') courseID: string) : Promise<{course : Course}> {
    const coursedata = await this.coursesService.findBymaHocPhan(courseID)
    return { course : coursedata } ;
  }
}
