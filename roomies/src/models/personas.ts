export interface PersonasI {
  id?: number;
  nombre?: string;
  apellido?: string;
  telefono?: string;
  correo?: string;
  ciudad?: string;
  num_identidad?: string;
  tipo_identificacion?: any;
  tipo_sexo?: any;
}
export interface Iusuario {
  id?: number;
  salario: number;
  empleo: string;
  tipo_usuario: any;
  username: string;
  password: string;
}