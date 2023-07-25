import { Entity, Column, PrimaryGeneratedColumn,CreateDateColumn } from 'typeorm';

@Entity('searchs')
export class Search {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  courseID: string;

  @CreateDateColumn({ type: 'datetime' })
  createtime: Date;

  @Column({ nullable: true })
  type: string;
}