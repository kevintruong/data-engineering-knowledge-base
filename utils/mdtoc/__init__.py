from utils.mdtoc.config import config
from utils.mdtoc.model import MdToc, HeadNode


def get_md_headlist(file: str):
    """
    开始处理 markdown 文件
    Start process the markdown file
    :param file: 文件完整路径或相对路径 the path of markdown file
    :param o: 输出文件完整路径
    :return: 处理结果 the result of process
    """

    toc = MdToc(config)
    # 存放 H1 节点信息
    head_list = list()
    now_node = None
    # toc.rebuild_head(file)
    with open(file, "r") as f:
        for index, line in enumerate(f.readlines(),start=1):
            res = toc.process_line(line)
            if res:
                # 如果匹配到标题
                tag, content = res
                level = toc.get_level(tag)
                node = HeadNode(level, content, index=index)
                if now_node is None:
                    # 初始化第一个节点为 now_node
                    now_node = node
                    head_list.append(now_node)
                else:
                    if node.level == -1:
                        # 将 H1 节点放入 head_list
                        head_list.append(node)
                    else:
                        if node.level < now_node.level:
                            # 如果节点等级小于当前节点，将其变为孩子
                            HeadNode.add_child(node, now_node)
                        else:
                            father = MdToc.get_father_node(node, now_node)
                            HeadNode.add_child(node, father)
                    now_node = node

    return head_list
