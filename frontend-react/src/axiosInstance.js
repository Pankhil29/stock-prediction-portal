import axios from "axios";

const baseURL = import.meta.env.VITE_BACKEND_BASE_API;
const axiosInstance = axios.create({
  // all request pass in this
  baseURL: baseURL,
  headers: {
    "content-type": "application/json",
  },
});

// request Interceptor
axiosInstance.interceptors.request.use(
  function (config) {
    // console.log("request without token => ", config);
    const accessToken = localStorage.getItem("accessToken");
    if (accessToken) {
      config.headers["Authorization"] = `Bearer ${accessToken}`;
    }
    return config;
  },
  function (error) {
    return Promise.reject(error);
  },
);

// Resopnse Interceptor
axiosInstance.interceptors.response.use(
  function (response) {
    return response; // if request is successful
  },
  async function (error) {
    //  if any error occurs then it call
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest.retry) {
      originalRequest.retry = true;
      const refreshToken = localStorage.getItem("refreshToken");
      try {
        const response = await axiosInstance.post("/token/refresh/", {
          refresh: refreshToken,
        });
        localStorage.setItem("accessToken", response.data.access);
        // console.log("resopnse ==>", response.data);
        originalRequest.headers["Authorization"] =
          `Bearer ${response.data.access}`;
        return axiosInstance(originalRequest);
      } catch (error) {
        localStorage.removeItem("accessToken");
        localStorage.removeItem("refreshToken");
        // window.location.href = "/login";
      }
    }
    return Promise.reject(error); // react ne kahe che ke error che
  },
);

export default axiosInstance;
