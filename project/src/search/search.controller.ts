import { Controller, Get, Post, Put, Delete, Param, Body } from '@nestjs/common';
import { SearchService } from './search.service';
import { Search } from './search.entity';
import { ApiTags } from '@nestjs/swagger';

@ApiTags('Search')
@Controller('Searchs')
export class SearchController {
  constructor(private readonly SearchService: SearchService) {}

  @Get('/')
  async findAll(): Promise<Search[]> {
    return this.SearchService.findAll();
  }

  @Get(':id')
  async findOne(@Param('id') id: number): Promise<Search> {
    return this.SearchService.findOne(id);
  }

  @Post()
  async create(@Body() Search: Search): Promise<Search> {
    return this.SearchService.create(Search);
  }

  @Put(':id')
  async update(@Param('id') id: number, @Body() Search: Search): Promise<Search> {
    return this.SearchService.update(id, Search);
  }

  @Delete(':id')
  async remove(@Param('id') id: number): Promise<void> {
    return this.SearchService.remove(id);
  }
}