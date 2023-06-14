import http from "../http_common";

class PersonasService {
  getAll() {
    return http.get("/persona");
  }

  get(id: string) {
    return http.get(`/persona/${id}`);
  }

  create(data: any) {
    return http.post("/persona", data);
  }

  update(id: string, data: any) {
    return http.put(`/persona/${id}`, data);
  }

  delete(id: string) {
    return http.delete(`/persona/${id}`);
  }

}

export default new PersonasService();