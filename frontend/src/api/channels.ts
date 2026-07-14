import { api } from "./client";

export async function getChannels(page = 1) {
  try {
    const response = await api.get("/channels/", {
      params: {
        page,
        size: 24,
      },
    });

    console.log("SUCCESS", response);

    return response.data;
  } catch (err: any) {
    console.error("AXIOS ERROR");

    console.log(err);
    console.log(err.message);
    console.log(err.response);
    console.log(err.response?.data);
    console.log(err.response?.status);

    throw err;
  }
}
