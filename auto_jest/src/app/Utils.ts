export function toUpperCase(arg: string) {
  return arg.toUpperCase();
}

export class StringUtils {
  public toUpperCase(arg: string) {
    if (!arg) {
      throw new Error("Invalid argument");
    }
    return toUpperCase(arg);
  }
}

export type stringInfo = {
  lowerCase: string;
  upperCase: string;
  characters: string[];
  length: number;
  extraInfo: Object | undefined;
};

// istanbul ignore can be used to ignore coverage of next line
/* istanbul ignore next */
export function getStringInfo(arg: string): stringInfo {
  return {
    lowerCase: arg.toLowerCase(),
    upperCase: arg.toUpperCase(),
    characters: Array.from(arg),
    length: arg.length,
    extraInfo: {},
  };
}
