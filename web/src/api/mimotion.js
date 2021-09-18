import { api } from "src/boot/axios";
export const SetStep = (username, password, step) => {
  return api.get("/api/set-step", {
    params: {
      user: username,
      password,
      step,
    },
  });
};
export const SetStepRandom = (username, password, min, max) => {
  return api.get("/api/set-step-random", {
    params: {
      user: username,
      password,
      min,
      max,
    },
  });
};
