class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        st = []

        for com in components:
            if com == "" or com == ".":
                continue
            elif com == "..":
                if st:
                    st.pop()
            else:
                st.append(com)

        return "/" + "/".join(st)

        