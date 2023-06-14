import { PersonasI } from "../models/personas";
import { createStore } from "vuex";
import axios from "axios";

const persona: PersonasI[] = [];
const personaOwner: PersonasI[] = [];

export const store = createStore({
  state() {
    return {
      persona,
      personaOwner,
    };
  },
  mutations: {
    getAllPersona() {
      const url = '/persona/';
      axios.get(url).then(response => {
        this.persona = response.data;
      })
    },
    async postPersona(state, data: PersonasI) {
      try {
        await axios.post("http://127.0.0.1:8000/persona/create/", data);
        state.persona.push(data);
      } catch (error) {
        console.log(error);
      }
    },
    async getPersona(state, url: string) {
      try {
        const resp = await axios.get(url);
        state.personaOwner = [...resp.data];
      } catch (error) {
        console.log(error);
      }
    },
    async putPersona(state, props: { url: string; data: PersonasI }) {
      try {
        await axios.put(props.url, props.data);
      } catch (error) {
        console.log(error);
      }
    },
  },
});