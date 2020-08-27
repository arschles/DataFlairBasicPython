import axios from "axios";

export const sendURL = async (YouTubeURL: any) => {
  const body = JSON.stringify(YouTubeURL);

  const config = {
    headers: {
      "content-type": "application/json",
    },
  };
  const response_ = await axios.post(
    "http://127.0.0.1:5000/converter",
    body,
    config
  );

  const response = await getFile();

  return response;
};

export const getFile = async () => {
  const response = await axios.get("http://127.0.0.1:5000/getFile");
  console.log(response);

  return response;
};
