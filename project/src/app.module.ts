import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ArgorithmController } from './argorithm.controller';
import { UserController } from './user/user.controller';
import { UserService } from './user/user.service';
import { User } from './user/user.entity';
import { TypeOrmModule } from '@nestjs/typeorm';
import { CourseController } from './course/course.controller';
import { CourseService } from './course/course.service';
import { Course } from './course/course.entity';
import { CoursesController } from './courses.controller';
import { TredController } from './tred.controller';
import { CycleController } from './cycle.controller';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'mysql',
      host: 'sinno.soict.ai',
      port: 3306,
      username: 'subjects_bdc',
      password: 'buiducche321',
      database: 'subjects_bdc',
      entities: [User , Course],
      synchronize: true,
    }),
    TypeOrmModule.forFeature([User]),
    TypeOrmModule.forFeature([Course])
  ],
  controllers: [AppController, CoursesController, ArgorithmController, UserController, CourseController, TredController, CycleController],
  providers: [AppService, UserService, CourseService],
})
export class AppModule {}
