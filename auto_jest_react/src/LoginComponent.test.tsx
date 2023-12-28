/* eslint-disable testing-library/no-node-access */
import { act, fireEvent, render, screen } from "@testing-library/react";
import user from "@testing-library/user-event";
import LoginComponent from "./LoginComponent";

describe("Login component test", () => {
  const loginServiceMock = {
    login: jest.fn(),
  };

  let container: HTMLElement;

  function setup() {
    return render(
      <LoginComponent loginService={loginServiceMock} setToken={setTokenMock} />
    ).container;
  }

  beforeEach(() => {
    container = setup();
  });

  const setTokenMock = jest.fn();
  it("should render correctly the login component", () => {
    const mainElement = screen.getByRole("main");
    expect(mainElement).toBeInTheDocument();
    expect(screen.queryByTestId("resultLabel")).not.toBeInTheDocument();
  });

  it("should render correctly - query by test id", () => {
    const inputs = screen.getAllByTestId("input");
    expect(inputs).toHaveLength(3);
    expect(inputs[0].getAttribute("value")).toBe("");
    expect(inputs[1].getAttribute("value")).toBe("");
    expect(inputs[2].getAttribute("value")).toBe("Login");
  });

  it("should render correctly - query by document query", () => {
    const inputs = container.querySelectorAll("input");
    expect(inputs).toHaveLength(3);
    expect(inputs[0].getAttribute("value")).toBe("");
    expect(inputs[1].getAttribute("value")).toBe("");
    expect(inputs[2].getAttribute("value")).toBe("Login");
  });

  it("click login button with incomplete credentials - show required message", () => {
    const inputs = screen.getAllByTestId("input");
    const loginButton = inputs[2];

    fireEvent.click(loginButton);

    const resultLabel = screen.getByTestId("resultLabel");
    expect(resultLabel.textContent).toBe("UserName and password required!");
  });

  it("click login button with incomplete credentials - show required message - with user click", () => {
    const inputs = screen.getAllByTestId("input");
    const loginButton = inputs[2];

    const clickLogin = function () {
      user.click(loginButton);
    };

    act(() => {
      clickLogin();
    });

    const resultLabel = screen.getByTestId("resultLabel");
    expect(resultLabel.textContent).toBe("UserName and password required!");
  });

  it("right credentials - successful login", async () => {
    loginServiceMock.login.mockResolvedValueOnce("1234");
    const inputs = screen.getAllByTestId("input");
    const userNameInput = inputs[0];
    const passwordInput = inputs[1];
    const loginButton = inputs[2];

    fireEvent.change(userNameInput, { target: { value: "someUser" } });
    fireEvent.change(passwordInput, { target: { value: "somePassword" } });
    fireEvent.click(loginButton);

    const resultLabel = await screen.findByTestId("resultLabel");
    expect(resultLabel.textContent).toBe("successful login");
  });

  it("right credentials - successful login - using user", async () => {
    loginServiceMock.login.mockResolvedValueOnce("1234");
    const inputs = screen.getAllByTestId("input");
    const userNameInput = inputs[0];
    const passwordInput = inputs[1];
    const loginButton = inputs[2];

    const userInteraction = () => {
      user.click(userNameInput);
      user.keyboard("someUser");
      user.click(passwordInput);
      user.keyboard("somePassword");
      user.click(loginButton);
    };

    act(() => {
      userInteraction();
    });

    expect(loginServiceMock.login).toBeCalledWith("someUser", "somePassword");

    const resultLabel = await screen.findByTestId("resultLabel");
    expect(resultLabel.textContent).toBe("successful login");
  });

  it("right credentials - unsuccessful login", async () => {
    loginServiceMock.login.mockResolvedValueOnce(undefined);
    const inputs = screen.getAllByTestId("input");
    const userNameInput = inputs[0];
    const passwordInput = inputs[1];
    const loginButton = inputs[2];

    fireEvent.change(userNameInput, { target: { value: "someUser" } });
    fireEvent.change(passwordInput, { target: { value: "somePassword" } });
    fireEvent.click(loginButton);

    const resultLabel = await screen.findByTestId("resultLabel");
    expect(resultLabel.textContent).toBe("invalid credentials");
  });

  it("right credentials - unsuccessful login - using user", async () => {
    loginServiceMock.login.mockResolvedValueOnce(undefined);
    const inputs = screen.getAllByTestId("input");
    const userNameInput = inputs[0];
    const passwordInput = inputs[1];
    const loginButton = inputs[2];

    const userInteraction = () => {
      user.click(userNameInput);
      user.keyboard("someUser");
      user.click(passwordInput);
      user.keyboard("somePassword");
      user.click(loginButton);
    };

    act(() => {
      userInteraction();
    });

    expect(loginServiceMock.login).toBeCalledWith("someUser", "somePassword");

    const resultLabel = await screen.findByTestId("resultLabel");
    expect(resultLabel.textContent).toBe("invalid credentials");
  });

  it("right credentials - unsuccessful login - using user - solve act warning", async () => {
    const result = Promise.resolve(undefined);
    loginServiceMock.login.mockResolvedValueOnce(result);
    const inputs = screen.getAllByTestId("input");
    const userNameInput = inputs[0];
    const passwordInput = inputs[1];
    const loginButton = inputs[2];

    const userInteraction = () => {
      user.click(userNameInput);
      user.keyboard("someUser");
      user.click(passwordInput);
      user.keyboard("somePassword");
      user.click(loginButton);
    };

    act(() => {
      userInteraction();
    });

    await result;
    expect(loginServiceMock.login).toBeCalledWith("someUser", "somePassword");

    const resultLabel = await screen.findByTestId("resultLabel");
    expect(resultLabel.textContent).toBe("invalid credentials");
  });
});
