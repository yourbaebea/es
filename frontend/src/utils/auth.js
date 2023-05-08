export function checkToken(props){
  console.log("[auth] checking if token");
  let token =null;

  if(props.token!=null){
    token=props.token;
  }
  else{
    const cookies = document.cookie.split(";").reduce((cookies, cookie) => {
      const [name, value] = cookie.trim().split("=");
      return { ...cookies, [name]: value };
    }, {});

    if (cookies==null || cookies.token==null) {
      window.location.replace('/login');
      return null;
    }

    token=cookies.token;
  }

  //check the auth here
  //TODO
  console.log("[auth] token was found: " + token);

  
  return token;

};

