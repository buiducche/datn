import { Get, Controller, Render, Post, Body } from '@nestjs/common';
import { CourseService } from './course/course.service';
import { Course } from './course/course.entity';
import { SearchService } from './search/search.service';

@Controller()
export class AppController {
  constructor(
    private readonly coursesService: CourseService,
    private readonly searchService: SearchService,
  ) {}

  @Get()
  @Render('index')
  root() {
    return { message: 'Hello world!' };
  }

  @Post()
  @Render('index')
  async search(@Body('courseID') courseID: string) : Promise<{course : Course}> {
    const coursedata = await this.coursesService.findBymaHocPhan(courseID)
    await this.searchService.createByCourseID(courseID,'home')
    return { course : coursedata } ;
  }
}
