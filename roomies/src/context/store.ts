import axios from "axios";
import { createStore } from "vuex";
import { ServiciosI } from "../models/servicios";
import  {router}  from "../router/router";


const servicio: ServiciosI[] = [];
const servicioOwner: ServiciosI[] = [];

const isAuthenticate = {
  auth: false,
  token: "",
};

export const store = createStore({
  state() {
    return {
      servicio,
      servicioOwner,
      isAuthenticate
    };
  },
  getters: {
    getToken(state) {
      return state.isAuthenticate.token;
    },
    getservicio(state) {
      return state.servicio;
    },
    getServicioOwner(state) {
      return state.servicioOwner;
    },
    getAuth(state) {
      return state.isAuthenticate.auth;
    },
  },
  actions: {
    async getServicio(context, props) {
      try {
        let query = new URLSearchParams({ search: props.search });
        const resp = await axios.get(props.url + "?" + query, {
          headers: {
            Authorization: "Bearer " + props.token,
          },
        });
        console.log(resp)
        context.commit("getAllServicio", resp.data);
      } catch (error) {
        console.log(error);
      }
    },

    async getownServicio(context, props) {
      try {
        const resp = await axios.get(props.url, {
          headers: {
            Authorization: `Bearer ` + props.token,
          },
        });
        context.commit("getServicio", resp.data);
      } catch (error) {
        console.log(error);
      }
    },
  },
  mutations: {
    async getAllServicio(state, data) {
      state.servicio = [...data];
    },
    async postServicio(state, data: ServiciosI) {
      try {
        await axios.post("http://localhost:8000/servicio/create/", data, {
          headers: {
            Authorization: `Bearer ` + state.isAuthenticate.token,
          },
        });
        state.servicio.push(data);
      } catch (error) {
        console.log(error);
      }
    },
    async getServicio(state, data) {
      state.servicioOwner = [...data];
    },
    async putServicio(state, props: { url: string; data: ServiciosI }) {
      try {
        await axios.put(props.url, props.data, {
          headers: {
            Authorization: `Bearer ` + state.isAuthenticate.token,
          },
        });
        router.push("/servicio");
      } catch (error) {
        console.log(error);
      }
    },

    async authLogin(state, props: { username: string; password: string }) {
      try {
        const resp = await axios.post("http://localhost:8000/auth/login/", {
          ...props,
        });

        if (!resp.data.token.access) {
          return null;
        }
        state.isAuthenticate = { auth: true, token: resp.data.token.access };
        localStorage.setItem(
          "auth",
          JSON.stringify({ auth: true, token: resp.data.token.access })
        );
        router.push("/servicio");
      } catch (error) {
        console.log(error);
      }
    },
    async registerUser(state, data) {
      try {
        console.log(data)
        await axios.post("http://localhost:8000/auth/register/", data);
      } catch (error) {
        console.log(error);
      }
    },

    saveToken(state, data: any) {
      state.isAuthenticate = { ...data };
    },
    logout(state) {
      state.isAuthenticate = { auth: false, token: "" };
      localStorage.clear();
    },

    async saveMaestra(state, props: { url: string; data: any }) {
      await axios.post(props.url, props.data);
    },
  },
});
