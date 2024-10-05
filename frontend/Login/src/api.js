import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

// Básicamente axios nos permite hacer peticiones al backend con un objeto API que nos da por defecto
// Lo único que hacemos aquí es modificar eso para que revise el localStorage buscando el token JWT, y si lo consigue
// se envía en los headers de cada petición que hagamos, ahorrando escribir código para cada petición.


// Se asigna la url base almacenada en el archivo .env, en caso que vayamos a hacer deploy del backend
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL : apiUrl,
});

// Se hace lo que dije del token JWT
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Y bueno se exporta la api modificada para usarla en lugar de la predeterminada xd
export default api;