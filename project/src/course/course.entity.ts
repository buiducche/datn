import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity('coursedetail')
export class Course {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  maHocPhan: string;

  @Column({ nullable: true })
  tenHocPhan: string;

  @Column({ nullable: true })
  thoiLuong: string;

  @Column({ nullable: true })
  soTinChi: number;

  @Column({ nullable: true })
  tinChiHocPhi: string;

  @Column({ nullable: true })
  trongSo: number;

  @Column({ nullable: true })
  hocPhanDieuKien: string;

  @Column({ nullable: true })
  tenTiengAnh: string;

  @Column({ nullable: true })
  vienQuanLy: string;

  @Column({ type: 'longtext', nullable: true })
  mucTieu: string;

  @Column({ type: 'longtext', nullable: true })
  noiDung: string;
}
