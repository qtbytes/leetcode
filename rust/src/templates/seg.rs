pub struct SegmentTree {
    seg: Vec<i32>,
}

impl SegmentTree {
    pub fn new(v: Vec<i32>) -> Self {
        let n = v.len();
        let mut st = SegmentTree {
            seg: vec![0; 4 * n + 1],
        };
        st.build(1, 0, n - 1, &v);
        st
    }
    pub fn maintain(&mut self, o: usize) {
        self.seg[o] = max(self.seg[o * 2], self.seg[o * 2 + 1])
    }

    pub fn build(&mut self, o: usize, l: usize, r: usize, v: &Vec<i32>) {
        if l == r {
            self.seg[o] = v[l];
            return;
        }
        let m = (l + r) / 2;
        self.build(o * 2, l, m, v);
        self.build(o * 2 + 1, m + 1, r, v);
        self.maintain(o);
    }
    pub fn find_first_and_update(&mut self, o: usize, l: usize, r: usize, x: i32) -> Option<usize> {
        if self.seg[o] < x {
            return None;
        }
        if l == r {
            self.seg[o] = -1;
            return Some(l);
        }
        let m = (l + r) >> 1;
        let res = if let Some(i) = self.find_first_and_update(o * 2, l, m, x) {
            Some(i)
        } else if let Some(i) = self.find_first_and_update(o * 2 + 1, m + 1, r, x) {
            Some(i)
        } else {
            None
        };
        self.maintain(o);
        res
    }
}
