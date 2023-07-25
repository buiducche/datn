import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Search } from './search.entity';

@Injectable()
export class SearchService {
  constructor(
    @InjectRepository(Search)
    private readonly SearchRepository: Repository<Search>,
  ) {}

  async findAll(): Promise<Search[]> {
    return this.SearchRepository.find();
  }

  async findOne(id: number): Promise<Search> {
    return this.SearchRepository.findOneBy({ id });
  }

  async create(Search: Search): Promise<Search> {
    return this.SearchRepository.save(Search);
  }

  async update(id: number, Search: Search): Promise<Search> {
    await this.SearchRepository.update(id, Search);
    return this.SearchRepository.findOneBy({ id });
  }

  async remove(id: number): Promise<void> {
    await this.SearchRepository.delete(id);
  }

  async createByCourseID(courseID: string,type: string): Promise<Search> {
    const search = new Search();
    search.courseID = courseID;
    search.type = type;
    return this.SearchRepository.save(search);
  }
}
