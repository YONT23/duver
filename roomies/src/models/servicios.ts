export interface DisponibilidadI {
  id?: number;
  disp_disponible: string;
  disp_precio: number;
}

export interface ServiciosI {
  id?: number;
  ciudad: string;
  estrato: string;
  pais: any;
  longitud: string;
  latitud: string;
  num_pisos: number;
  num_baños: number;
  num_habitaciones: number;
  url_imagenes: string;
  superficie: string;
  descripcion: string;
  tipo_inmueble: any;
  tipo_estado: any;
}