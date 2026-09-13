from setuptools import setup, find_packages

setup(
    name='gym_anytrading',
    version='2.1.0',
    packages=find_packages(),

    author='AminHP',
    author_email='mdan.hagh@gmail.com',
    license='MIT',

    # 核心依赖: 版本下限反映代码实际使用的 API(已适配 gymnasium 1.x)
    # pandas 加上限 <3.0.0: pandas 3.0 有破坏性变更(copy-on-write/字符串dtype), 避免误升
    install_requires=[
        'gymnasium>=1.0.0',
        'numpy>=1.26.0',
        'pandas>=2.0.0,<3.0.0',
        'matplotlib>=3.7.0'
    ],

    # 可选依赖: 训练智能体 / 绩效报告
    # 安装方式: pip install -e '.[train]'  或  pip install -e '.[train,report]'
    extras_require={
        'train': [
            'stable-baselines3>=2.0.0',
            'torch>=2.0.0',
        ],
        'report': [
            'quantstats',
        ],
    },

    package_data={
        'gym_anytrading': ['datasets/data/*']
    }
)
