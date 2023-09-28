import ContextProps from "@/types/ContextProps";
import MessageContextData from "@/types/MessageContextData";
import { createContext, useContext, useState } from "react";

export const Context = createContext<MessageContextData | null>(null);

export const Provider = ({ children }: ContextProps) => {
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  const context = {
    successMessage,
    setSuccessMessage,
  };

  return <Context.Provider value={context}>{children}</Context.Provider>;
};

export const { Consumer } = Context;

export const useMessageContext = () => useContext(Context);
