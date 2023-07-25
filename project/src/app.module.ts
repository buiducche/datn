import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ArgorithmController } from './argorithm.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { CourseController } from './course/course.controller';
import { CourseService } from './course/course.service';
import { Course } from './course/course.entity';
import { CoursesController } from './courses.controller';
import { TredController } from './tred.controller';
import { CycleController } from './cycle.controller';
import { SearchController } from './search/search.controller';
import { SearchService } from './search/search.service';
import { Search } from './search/search.entity';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'mysql',
      host: 'sinno.soict.ai',
      port: 3306,
      username: 'subjects_bdc',
      password: 'buiducche321',
      database: 'subjects_bdc',
      entities: [Course , Search],
      synchronize: true,
    }),
    TypeOrmModule.forFeature([Course]),
    TypeOrmModule.forFeature([Search])
  ],
  controllers: [AppController, CoursesController, ArgorithmController, CourseController, TredController, CycleController, SearchController],
  providers: [AppService, CourseService, SearchService],
})
export class AppModule {}
