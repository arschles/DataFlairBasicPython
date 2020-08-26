import axios from "axios";

export const sendURL = async (YouTubeURL: any) => {
  const body = JSON.stringify(YouTubeURL);

  const config = {
    headers: {
      "content-type": "application/json",
    },
  };
  const response = await axios.post(
    "http://127.0.0.1:5000/converter",
    body,
    config
  );
  return response;
};
