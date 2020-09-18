import axios from "axios";

export const sendURL = async (YouTubeURL: any) => {
  const body = JSON.stringify(YouTubeURL);

  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  const response = await axios.post(
    "http://127.0.0.1:5000/converter",
    body,
    config
  );

  const downloadFile = await getFile(response);

  return downloadFile;
};

export const getFile = async (response: any) => {
  const redirect = window.location.assign(
    `http://127.0.0.1:5000/getFile/${response.data}`
  );

  return "Done";
};
