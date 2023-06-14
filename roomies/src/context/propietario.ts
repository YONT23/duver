import axios from "axios";
import { createStore } from "vuex";
import { PropietarioI } from "../models/propietarios";

const propietario: PropietarioI[] = [];
const propietarioOwner: PropietarioI[] = [];

export const store = createStore({
  state() {
    return {
      propietario,
      propietarioOwner,
    };
  },
  mutations: {
    async getAllPropietario(state, url: string) {
      try {
        const resp = await axios.get(url);
        state.propietario = [...resp.data];
      } catch (error) {
        console.log(error);
      }
    },
    async postPropietario(state, data: PropietarioI) {
      try {
        await axios.post("http://127.0.0.1:8000/propietarios/ppcreate/", data);
        state.propietario.push(data);
      } catch (error) {
        console.log(error);
      }
    },
    async getPropietario(state, url: string) {
      try {
        const resp = await axios.get(url);
        state.propietarioOwner = [...resp.data];
      } catch (error) {
        console.log(error);
      }
    },
    async putPropietario(state, props: { url: string; data: PropietarioI }) {
      try {
        await axios.put(props.url, props.data);
      } catch (error) {
        console.log(error);
      }
    },
  },
});